import React, { useEffect, useState } from 'react';
import {
    Text,
    View,
    Image,
    Button,
    FlatList,
} from 'react-native';

import SQLite from 'react-native-sqlite-storage'
import TextTicker from 'react-native-text-ticker'
import styles from './StyleSheet';

const db = SQLite.openDatabase(
    {
        name: 'BookDB',
    },
    () => { console.log('HomePage database connected') },
    error => { console.log(error) }
);

const HomeScreen = ({ navigation, route }) => {
    const [lastEntry, setLastEntry] = useState([]);
    const [totalPages, setTotal] = useState();
    const [avgPages, setAVG] = useState();

    // Button customization and information regarding the OnPress expression:
    // Author: Meta Platforms, Inc. 2022
    // Link: https://reactnative.dev/docs/button

    const totalCount = () => {
        db.transaction((tx) => {
            tx.executeSql(
                "SELECT NumberOfPages FROM bookCatalogue",
                [],
                (sqlTx, res) => {
                    let len = res.rows.length;
                    let sum = 0;
                    let average = 0;

                    if (len > 0) {
                        let results = [];
                        for (let i = 0; i < len; i++) {
                            let item = res.rows.item(i);
                            results.push({ NumberOfPages: item.NumberOfPages });
                            sum += results[i].NumberOfPages
                        }
                        average = sum / len;
                        average = average.toFixed(2);
                    }
                    setAVG(average);
                    setTotal(sum);
                },
                error => { console.log('error creating table' + error.message); });
        });
    };

    const lastBook = () => {
        db.transaction((tx) => {
            tx.executeSql(
                "SELECT * FROM bookCatalogue ORDER BY ID DESC LIMIT 1",
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
                        setLastEntry(results);
                    }
                },
                error => { console.log('error creating table' + error.message); },
            );
        });
    };

    const renderLastBook = ({ item }) => {
        return (
            <View style={{ flexDirection: 'row', paddingVertical: 12, borderBottomWidth: 1 }}>
                <TextTicker scrollSpeed={20} loop bounce numberOfLines={1} style={styles.smallText2} repeatSpacer={50}>
                    LAST BOOK ADDED DETAILS: Title: {item.Title}, Author: {item.Author}, Genre: {item.Genre}, Pages: {item.NumberOfPages}.</TextTicker>
            </View>
        );
    };

    useEffect(() => {
        totalCount(), console.log('Total pages calculated'),
        lastBook(), console.log('Last Book received')
    }, []);

    return (
        <View style={{ flex: 1, backgroundColor: '#94B49F' }}>
            <Text style={styles.smallText3}>Total Pages: {totalPages}</Text>
            <Text style={styles.smallText3}>Avg Pages: {avgPages}</Text>
            <Image style={styles.mainPicture} source={require('../img/Logo1.png')} />

            {/*Image styling:}
        Author: Meta Platforms, Inc. 2022
        Link: https://reactnative.dev/docs/image */}

            <FlatList
                data={lastEntry}
                renderItem={renderLastBook}
                key={lastBook => lastBook.id}
            />

            {/* TextTicker implementation 
              Author: NPM (n.d.)
              Link: https://www.npmjs.com/package/react-native-text-ticker*/}

            <View style={styles.buttonMod}>
                <Button title="ADD BOOK" color='#ECB390'
                    onPress={() => {
                        navigation.navigate('Add Book')
                    }} />
            </View>
            <View style={styles.buttonMod}>
                <Button title="EDIT BOOK" color='#ECB390'
                    onPress={() => {
                        navigation.navigate('Edit Page')
                    }} />
            </View>
            <View style={styles.buttonMod}>
                <Button title="HISTORY/REMOVE BOOK" color='#ECB390'
                    onPress={() => {
                        navigation.navigate('History/ Remove Book')
                    }} />
            </View>
            <View style={styles.buttonMod}>
                <Button title="GENRES" color='#ECB390'
                    onPress={() => {
                        navigation.navigate('Genre')
                    }} />
            </View>
        </View>
    );
};

export default HomeScreen;