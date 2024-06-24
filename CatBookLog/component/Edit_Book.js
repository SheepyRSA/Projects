import React, { useState, useEffect } from 'react';
import {
  Text,
  TextInput,
  View,
  Image,
  Button,
  ToastAndroid,
} from 'react-native';

import SQLite from 'react-native-sqlite-storage'
import SelectDropdown from 'react-native-select-dropdown'
import styles from './StyleSheet';
import mobileAds from 'react-native-google-mobile-ads';

mobileAds()
  .initialize()
  .then(adapterStatuses => {
    console.log('Initialization for EditPage complete!')
  });

const db = SQLite.openDatabase(
  {
    name: 'BookDB',
  },
  () => { console.log('EditPage database connected') },
  error => { console.log(error) }
);

const EditPage = ({ navigation, route }) => {
  const [title2, setTitle2] = useState();
  const [author2, setAuthor2] = useState();
  const [pageNum2, setNum2] = useState();
  const [bookGenre2, setGenre2] = useState();
  const [updateId, setUpdateID] = useState();
  const [genresList, setGenreList] = useState([""]);

  const handleSelect = (e) => { setGenre2(e) }


  let updateState = (Title, Author, Genre, NumberOfPages) => {
    setAuthor2(Author);
    setGenre2(Genre);
    setNum2(NumberOfPages);
    setUpdateID(ID);
    setTitle2(Title);

  };

  const selectButton = () => {
    if (!updateId) {
      ToastAndroid.show("Enter Book ID(can be found on history page)", ToastAndroid.SHORT);
      return false;
    }

    db.transaction((tx) => {
      tx.executeSql(
        "SELECT * FROM bookCatalogue where ID = ?",
        [updateId],
        (sqlTx, res) => {
          ToastAndroid.show("Book ID found", ToastAndroid.SHORT);
          let len = res.rows.length;
          if (len > 0) {
            let res = res.rows.item(0);
            updateState(
              res.Author,
              res.Genre,
              res.ID,
              res.NumberOfPages,
              res.Title
            );
          }
        },
        error => {
          console.log('error creating table' + error.message);
          ToastAndroid.show("No Book ID found", ToastAndroid.SHORT);
          updateState('', '', '', '', '');
        },)
    }
    )
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
          } else { ToastAndroid.show("Reminder to enter Genres at the Genre Page", ToastAndroid.SHORT); }
        },
        error => { console.log('error creating table' + error.message); })
    })
  };

  useEffect(() => {
    selectGenre();
  }, []);

  const updateEntry = () => {

    if (!updateId) {
      ToastAndroid.show("Enter Book ID(can be found on history page)", ToastAndroid.SHORT);
      return false;
    } else if (!title2) {
      ToastAndroid.show("Enter Title", ToastAndroid.SHORT);
      return false;
    } else if (!author2) {
      ToastAndroid.show("Enter Author", ToastAndroid.SHORT);
      return false;
    } else if (!bookGenre2) {
      ToastAndroid.show("Enter Genre", ToastAndroid.SHORT);
      return false;
    } else if (!pageNum2) {
      ToastAndroid.show("Enter number of Pages", ToastAndroid.SHORT);
      return false;
    }

    db.transaction((tx) => {
      tx.executeSql(
        "UPDATE bookCatalogue set Title=?, Author=? , Genre=?, NumberOfPages=? where ID=?",
        [title2, author2, bookGenre2, pageNum2, updateId],
        (tx, res) => {
          ToastAndroid.show(title2 + " has been updated to the database", ToastAndroid.LONG);
          navigation.replace('Home');
        },
        error => { ToastAndroid.show("Update Failed", ToastAndroid.SHORT); }
      );
    });
  };

  return (
    <View style={{ flex: 1, backgroundColor: '#94B49F' }}>
      <Image style={styles.secondaryPicture} source={require('../img/Logo1.png')} />
      <TextInput style={styles.textInputMod} placeholderTextColor="#FCF8E8" placeholder='Enter Book ID'
        value={updateId}
        keyboardType={'number-pad'}
        onChangeText={setUpdateID} />
      <View style={styles.buttonMod2}>
        <Button title="SELECT" color='#ECB390'
          onPress={selectButton} />
      </View>
      <View style={styles.horizontalLayout}>
        <Text style={styles.secondText}>Title:</Text>
        <TextInput style={styles.secondText2} placeholderTextColor="#FCF8E8" placeholder='Enter here'
          value={title2}
          onChangeText={setTitle2} />
      </View>
      <View style={styles.horizontalLayout}>
        <Text style={styles.secondText}>Author:</Text>
        <TextInput style={styles.secondText2} placeholderTextColor="#FCF8E8" placeholder='Enter here'
          value={author2}
          onChangeText={setAuthor2} />
      </View>
      <View style={styles.horizontalLayout}>
        <Text style={styles.secondText}>Genre:</Text>
        <SelectDropdown
          data={genresList}
          selectedItem={bookGenre2}
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
        <Text style={styles.secondText}>Page numbers:</Text>
        <TextInput style={styles.secondText2} placeholderTextColor="#FCF8E8" placeholder='Enter here'
          value={pageNum2}
          keyboardType={'number-pad'}
          onChangeText={setNum2} />
      </View>
      <View style={styles.buttonMod2}>
        <Button title="UPDATE" color='#ECB390'
          onPress={updateEntry} />
      </View>
    </View>
  );
};

export default EditPage;