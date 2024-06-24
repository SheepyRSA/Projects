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
    console.log('Initialization for AddPage complete!')
  });

const db = SQLite.openDatabase(
  {
    name: 'BookDB',
  },
  () => { console.log('AddPage database connected') },
  error => { console.log(error) }
);

const AddBook = ({ navigation, route }) => {
  const [title, setTitle] = useState();
  const [author, setAuthor] = useState();
  const [pageNum, setNum] = useState();
  const [bookGenre, setGenre] = useState();
  const [genresList, setGenreList] = useState([]);

  const handleSelect = (e) => { setGenre(e) }

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

  // SQL implementation
  // Author: www.sqltutorial.org. (2022)
  // Link: https://www.sqltutorial.org

  const addBook = () => {
    if (!title) {
      ToastAndroid.show("Enter Title", ToastAndroid.SHORT);
      return false;
    } else if (!author) {
      ToastAndroid.show("Enter Author", ToastAndroid.SHORT);
      return false;
    } else if (!bookGenre) {
      ToastAndroid.show("Enter Genre", ToastAndroid.SHORT);
      return false;
    } else if (!pageNum) {
      ToastAndroid.show("Enter number of Pages", ToastAndroid.SHORT);
      return false;
    } 

    // Toast Message for missing
    // Author: Meta Platforms, Inc. (2022)
    // Link: https://reactnative.dev/docs/toastandroid

    db.transaction((tx) => {
      tx.executeSql(
        "INSERT INTO bookCatalogue (Title, Author, Genre, NumberOfPages) VALUES (?,?,?,?)",
        [title, author, bookGenre, pageNum],
        (sqlTx, res) => {
          ToastAndroid.show(title + " has been added to the database", ToastAndroid.LONG);
          navigation.replace('Home');
        },
        error => { console.log('error creating table' + error.message); },
      )
    })
  };

  return (
    <View style={{ flex: 1, backgroundColor: '#94B49F' }}>
      <Image style={styles.secondaryPicture} source={require('../img/Logo1.png')} />
      <View style={styles.horizontalLayout}>
        <Text style={styles.secondText}>Title:</Text>
        <TextInput style={styles.secondText2} placeholderTextColor="#FCF8E8" placeholder='Enter here'
          value={title}
          onChangeText={setTitle} />
      </View>
      <View style={styles.horizontalLayout}>
        <Text style={styles.secondText}>Author: </Text>
        <TextInput style={styles.secondText2} placeholderTextColor="#FCF8E8" placeholder='Enter here'
          value={author}
          onChangeText={setAuthor} />
      </View>
      <View style={styles.horizontalLayout}>
        <Text style={styles.secondText}>Genre: </Text>
        <SelectDropdown
          data={genresList}
          selectedItem={bookGenre}
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
        <Text style={styles.secondText}>Page numbers: </Text>
        <TextInput style={styles.secondText2} placeholderTextColor="#FCF8E8" placeholder='Enter here'
          value={pageNum}
          keyboardType={'number-pad'} // Changing the keyboard to only allow numbers, Author: Meta Platforms, Inc.(2022), Link: https://reactnative.dev/docs/textinput
          onChangeText={setNum} />
      </View>
      <View style={styles.buttonMod2}>
        <Button title="ADD" color='#ECB390'
          onPress={addBook} />
      </View>
    </View>
  );
};

export default AddBook;