import React, { useState, useEffect, } from 'react';
import {
  ToastAndroid,
  Text,
  TextInput,
  View,
  Image,
  Button,
  FlatList,
  Keyboard,
} from 'react-native';

import SQLite from 'react-native-sqlite-storage'
import SelectDropdown from 'react-native-select-dropdown'
import TextTicker from 'react-native-text-ticker'
import styles from './StyleSheet'

const db = SQLite.openDatabase(
  {
    name: 'BookDB',
  },
  () => { console.log('GenrePage database connected') },
  error => { console.log(error) }
);

const GenrePage = ({ navigation, route }) => {
  const [updateGenre, setUpdateGenre] = useState();
  const [newGenre, setNewGenre] = useState();
  const [totalBook, setTotalGenre] = useState();
  const [genreTotal, setGenreTotal] = useState();
  const [genresList, setGenreList] = useState([]);

  const handleSelect = (e) => { setUpdateGenre(e) }

  const addGenre = () => {
    if (!newGenre) {
      ToastAndroid.show("Enter Genre", ToastAndroid.SHORT);
      return false;
    }
    Keyboard.dismiss();

    // Toast Message for missing
    // Author: Meta Platforms, Inc. (2022)
    // Link: https://reactnative.dev/docs/toastandroid

    db.transaction((tx) => {
      tx.executeSql(
        "INSERT INTO Genres (Genre) VALUES (?)",
        [newGenre],
        (sqlTx, res) => {
          ToastAndroid.show(newGenre + " has been added to the database", ToastAndroid.LONG);
          navigation.replace('Genre');
        },
        error => { console.log('error creating table' + error.message); },
      )
    })


  };

  const selectGenre = () => {
    db.transaction((tx) => {
      tx.executeSql(
        "SELECT * FROM Genres",
        [],
        (sqlTx, res) => {
          let len = res.rows.length;

          if (len > 0) {
            let results = []
            let transferAgent = []
            for (let i = 0; i < len; i++) {
              let item = res.rows.item(i);
              results.push({ Genre: item.Genre });
              transferAgent[i] = results[i].Genre
            }
            setGenreList(transferAgent);
          } else { ToastAndroid.show("No Genres loaded", ToastAndroid.SHORT); }
        },
        error => { console.log('error creating table' + error.message); })
    })
  };

  useEffect(() => {
    selectGenre();
  }, []);

  const deleteGenre = () => {
    if (!updateGenre) {
      ToastAndroid.show("Select Genre from Dropdown", ToastAndroid.SHORT);
      return false;
    }

    db.transaction((tx) => {
      tx.executeSql(
        "SELECT * FROM Genres where Genre = ?",
        [updateGenre],
        (sqlTx, res) => { console.log('Genre Found'); },
        error => {
          console.log('error selecting from table' + error.message);
          ToastAndroid.show('No Genre found');
        },)
    });

    db.transaction((tx) => {
      tx.executeSql(
        'DELETE FROM Genres WHERE Genre=?',
        [updateGenre],
        (tx, results) => {
          console.log('Results', results.rowsAffected);
          if (results.rowsAffected > 0) {
            ToastAndroid.show("Entry: " + updateGenre + " has been deleted from the database, dropdown should not be updated", ToastAndroid.LONG);
            navigation.replace('Genre');
            console.log(`${updateGenre} has been deleted successfully`);
          } else ToastAndroid.show('Update Failed', ToastAndroid.SHORT);
        },
        error => { console.log('error deleting from table' + error.message); }
      );
    })
  };

  const totalGenres = () => {
    if (!updateGenre) {
      ToastAndroid.show("Select Genre from Dropdown", ToastAndroid.SHORT);
      return false;
    }

    db.transaction((tx) => {
      tx.executeSql(
        'SELECT * FROM bookCatalogue where Genre=?',
        [updateGenre],
        (sqlTx, res) => {
          console.log('totalGenres calculated');
          let len = res.rows.length;
          let dup = [];
          let sum = 0;

          if (len > 0) {
            let results = [];
            let x = 0

            for (let i = 0; i < len; i++) {
              let item = res.rows.item(i);
              results.push({ ID: item.ID, Title: item.Title, Author: item.Author, Genre: item.Genre, NumberOfPages: item.NumberOfPages });
            }
            setGenreTotal(results);

            for (let i = 0; i < len; i++) {
              dup[i] = results[i].Genre
            }

            while (x < len) {
              if (updateGenre === dup[x]) {
                sum += 1
              }
              x++
            }
            setTotalGenre(sum);
          }
          else {setTotalGenre(0);}
        },
        error => { console.log('error creating table' + error.message); });
    });
  };

  const renderGenres = ({ item }) => {
    return (
      <View style={{ flexDirection: 'row', paddingVertical: 12, paddingHorizontal: 10, borderBottomWidth: 1, borderColor: "#ddd" }}>
        <Text style={{ marginRight: 8, color: '#FCF8E8' }}>{item.ID}</Text>
        <TextTicker style={styles.colorHistoryText} scrollSpeed={80} loop={true} bounce={true} numberOfLines={1} repeatSpacer={50}>Title: {item.Title}, Author: {item.Author}, Genre: {item.Genre}, Pages: {item.NumberOfPages}</TextTicker>
      </View>
    );
  };

  return (
    <View style={{ flex: 1, backgroundColor: '#94B49F' }}>
      <Image style={styles.secondaryPicture} source={require('../img/Logo1.png')} />
      <TextInput style={styles.secondText2} placeholderTextColor="#FCF8E8" placeholder=' Add new Genre here'
        value={newGenre}
        onChangeText={setNewGenre}
        clearTextOnFocus={true} />
      <View style={styles.buttonMod2}>
        <Button title="ADD" color='#ECB390'
          onPress={addGenre} />
      </View>
      <View style={styles.buttonMod2}>
        <SelectDropdown
          data={genresList}
          selectedItem={updateGenre}
          defaultButtonText={'Select Genre'}
          onSelect={handleSelect}
          buttonTextAfterSelection={(selectedItem, index) => { return selectedItem }}
          rowTextForSelection={(item, index) => { return item }}
          buttonStyle={{ backgroundColor: '#ECB390' }}
          buttonTextStyle={{ color: '#fff' }}
          dropdownStyle={{ backgroundColor: '#94B49F' }}
          rowTextStyle={{ color: '#fff' }} />
      </View>
      <View style={styles.horizontalLayout}>
        <View style={styles.buttonMod4}>
          <Button title="SELECT" color='#ECB390'
            onPress={totalGenres} />
        </View>
        <View style={styles.buttonModLeft}>
          <Button style={{ marginLeft: 10 }} title="REMOVE" color='#ECB390'
            onPress={deleteGenre} />
        </View>
      </View>
      <Text style={styles.infoGenreText}>Press select again when a new genre is chosen from the dropdown list to display the new information below:</Text>
      <View style={styles.horizontalLayout3}>
        <Text style={styles.colorHistoryText}>Genre: {updateGenre}</Text>
        <Text style={styles.colorHistoryText}>     Number of books: {totalBook}</Text>
      </View>
      <FlatList
        data={genreTotal}
        renderItem={renderGenres}
        key={gTotal => gTotal.id}
      />

    </View>
  );
};

export default GenrePage;