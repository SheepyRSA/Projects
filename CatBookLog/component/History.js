import React, { useEffect, useState } from 'react';
import {
  Text,
  TextInput,
  View,
  Image,
  Button,
  ToastAndroid,
  FlatList,
} from 'react-native';

import SQLite from 'react-native-sqlite-storage'
import TextTicker from 'react-native-text-ticker'
import styles from './StyleSheet';
import mobileAds from 'react-native-google-mobile-ads';

mobileAds()
  .initialize()
  .then(adapterStatuses => {
    console.log('Initialization for History complete!')
  });

const db = SQLite.openDatabase(
  {
    name: 'BookDB',
  },
  () => { console.log('HistoryPage database connected') },
  error => { console.log(error) }
);

const HistoryPage = ({ navigation, route }) => {
  const [BHistory, setHistory] = useState([]);
  const [bookID, setBookID] = useState();

  const displayBook = () => {
    db.transaction((tx) => {
      tx.executeSql(
        "SELECT * FROM bookCatalogue ORDER BY id DESC",
        [],
        (sqlTx, res) => {
          console.log('Successfully retrieved bookCatalogue');
          let len = res.rows.length;

          if (len > 0) {
            let results = [];
            for (let i = 0; i < len; i++) {
              let item = res.rows.item(i);
              results.push({ ID: item.ID, Title: item.Title, Author: item.Author, Genre: item.Genre, NumberOfPages: item.NumberOfPages });
            }
            setHistory(results);
          }
        },
        error => { console.log('error creating table' + error.message); })
    })
  };

  const renderHistory = ({ item }) => {
    return (
      <View style={{ flexDirection: 'row', paddingVertical: 12, paddingHorizontal: 10, borderBottomWidth: 1, borderColor: "#ddd" }}>
        <Text style={{ marginRight: 8, color: '#FCF8E8' }}>{item.ID}</Text>
        <TextTicker style={styles.colorHistoryText} scrollSpeed={80} loop={true} bounce={true} numberOfLines={1} repeatSpacer={50}>Title: {item.Title}, Author: {item.Author}, Genre: {item.Genre}, Pages: {item.NumberOfPages}</TextTicker>
      </View>
    );
  };

  const deleteEntry = () => {
    if (!bookID) {
      ToastAndroid.show("Enter Book ID", ToastAndroid.SHORT);
      return false;
    }

    db.transaction((tx) => {
      tx.executeSql(
        "SELECT * FROM bookCatalogue where ID = ?",
        [bookID],
        (sqlTx, res) => { console.log('ID Found'); },
        error => {
          console.log('error selecting from table' + error.message);
          ToastAndroid.show('No Book ID found');
        },)
    });

    db.transaction((tx) => {
      tx.executeSql(
        'DELETE FROM bookCatalogue WHERE ID=?',
        [bookID],
        (tx, results) => {
          console.log('Results', results.rowsAffected);
          if (results.rowsAffected > 0) {
            ToastAndroid.show("Entry: " + bookID + " has been deleted from the database, refresh history by pressing History button", ToastAndroid.LONG);
            console.log(`${bookID} has been deleted successfully`);
          } else ToastAndroid.show('Update Failed', ToastAndroid.SHORT);
        },
        error => { console.log('error deleting from table' + error.message); }
      );
    })
  };

  useEffect(() => {
    displayBook();
  }, []);

  return (
    <View style={{ flex: 1, backgroundColor: '#94B49F' }}>
      <Image style={styles.secondaryPicture} source={require('../img/Logo1.png')} />
      <View style={styles.horizontalLayout}>
        <View style={styles.buttonMod3}><Button title="SHOW HISTORY" color='#ECB390' onPress={displayBook} /></View>
        <View style={styles.buttonMod2}><Button title="REMOVE" color='#ECB390' onPress={deleteEntry} /></View>
        <TextInput style={styles.secondText} placeholderTextColor="#FCF8E8" placeholder='Enter ID'
          value={bookID}
          keyboardType={'number-pad'}
          onChangeText={setBookID} />
      </View>
      <Text style={styles.infoHistoryText}>*Refresh list by pressing SHOW HISTORY again*</Text>
      <FlatList
        data={BHistory}
        renderItem={renderHistory}
        key={title => title.id}
      />
    </View>
  );
};

export default HistoryPage;
