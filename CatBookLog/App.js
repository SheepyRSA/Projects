import React, { useEffect} from 'react';
import {
  View,
  Image,
} from 'react-native';

import {
  NavigationContainer
} from '@react-navigation/native';

import {
  createNativeStackNavigator
} from '@react-navigation/native-stack';

import SQLite from 'react-native-sqlite-storage'
import FadeInView from './component/FadeInView'
import AddBook from './component/Add_Book'
import EditPage from './component/Edit_Book'
import HistoryPage from './component/History'
import GenrePage from './component/Genre'
import styles from './component/StyleSheet'
import HomeScreen from './component/Homepage'
import mobileAds, { MaxAdContentRating } from 'react-native-google-mobile-ads'
import { AdsConsent, AdsConsentStatus } from 'react-native-google-mobile-ads'

mobileAds()
  .setRequestConfiguration({
    maxAdContentRating: MaxAdContentRating.PG,
    tagForChildDirectedTreatment: true,
    tagForUnderAgeOfConsent: true,
    testDeviceIdentifiers: ['EMULATOR'],
  })
  .then(() => {
    console.log('config successfully set!')
  });

const consentInfo = await AdsConsent.requestInfoUpdate({
    debugGeography: AdsConsentDebugGeography.EEA,
    testDeviceIdentifiers: ['TEST-DEVICE-HASHED-ID'],
  });

if (consentInfo.isConsentFormAvailable && consentInfo.status === AdsConsentStatus.REQUIRED) {
  const { status } = await AdsConsent.showForm();
};

const {
  activelyScanDeviceCharacteristicsForIdentification,
  applyMarketResearchToGenerateAudienceInsights,
  createAPersonalisedAdsProfile,
  createAPersonalisedContentProfile,
  developAndImproveProducts,
  measureAdPerformance,
  measureContentPerformance,
  selectBasicAds,
  selectPersonalisedAds,
  selectPersonalisedContent,
  storeAndAccessInformationOnDevice,
  usePreciseGeolocationData,
} = await AdsConsent.getUserChoices();

if (storeAndAccessInformationOnDevice === false) {
  /**
   * The user declined consent for purpose 1,
   * the Google Mobile Ads SDK won't serve ads.
   */
};

const db = SQLite.openDatabase(
  {
    name: 'BooktDB',
  },
  () => { console.log('Database Found') },
  error => { console.log(error) }
);

const App = () => {

  const createTable = () => {
    db.transaction((tx) => {
      tx.executeSql(
        'CREATE TABLE IF NOT EXISTS bookCatalogue (ID INTEGER PRIMARY KEY AUTOINCREMENT, Title TEXT, Author TEXT, Genre TEXT, NumberOfPages INTEGER)',
        [],
        (sqlTx, res) => { console.log('Table successfully created'); },
        error => { console.log('error creating table' + error.message); },
      );
    }
    );
  };
  const createGenreTable = () => {
    db.transaction((tx) => {
      tx.executeSql(
        'CREATE TABLE IF NOT EXISTS Genres (Genre TEXT)',
        [],
        (sqlTx, res) => { console.log('Genre Table successfully created'); },
        error => { console.log('error creating table' + error.message); },
      );
    }
    );
  };

  useEffect(() => {
    createTable();
    createGenreTable();
  }, []);

  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName='Welcome'>
        <Stack.Screen name="Welcome" component={WelcomeScreen} options={{ headerStyle: { backgroundColor: '#ECB390' }, headerTintColor: '#FCF8E8' }} />
        <Stack.Screen name="Home" component={HomeScreen} options={{ headerStyle: { backgroundColor: '#ECB390' }, headerTintColor: '#FCF8E8' }} />
        <Stack.Screen name="Add Book" component={AddBook} options={{ headerStyle: { backgroundColor: '#ECB390' }, headerTintColor: '#FCF8E8' }} />
        <Stack.Screen name="Edit Page" component={EditPage} options={{ headerStyle: { backgroundColor: '#ECB390' }, headerTintColor: '#FCF8E8' }} />
        <Stack.Screen name="History/ Remove Book" component={HistoryPage} options={{ headerStyle: { backgroundColor: '#ECB390' }, headerTintColor: '#FCF8E8' }} />
        <Stack.Screen name="Genre" component={GenrePage} options={{ headerStyle: { backgroundColor: '#ECB390' }, headerTintColor: '#FCF8E8' }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

//The following was taken from the IIE Module manual to add navigation, styling and animation to the program:
//Author: The IIE. 2022. Mobile App Scripting [MAST5112 Module Manual]. The Independent Institute of Education: Unpublished.

const WelcomeScreen = ({ navigation, route }) => {

  setTimeout(() => { navigation.replace('Home') }, 3000);

  return (
    <View style={{ flex: 1, backgroundColor: '#94B49F' }}>
      <FadeInView>
        <Image style={styles.welcomePicture} source={require('./img/Logo1.png')} />
      </FadeInView>
    </View>
  );
};

const Stack = createNativeStackNavigator();

export default App;