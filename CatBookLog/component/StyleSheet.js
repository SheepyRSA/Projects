import {
  StyleSheet,
} from 'react-native';

const styles = StyleSheet.create({
    sectionContainer: {
      marginTop: 32,
      paddingHorizontal: 24,
    },
    sectionTitle: {
      fontSize: 24,
      fontWeight: '600',
    },
    sectionDescription: {
      marginTop: 8,
      fontSize: 18,
      fontWeight: '400',
    },
    highlight: {
      fontWeight: '700',
    },
    mainPicture: {
      alignItems: 'center',
      resizeMode: 'center',
      width: 'auto',
      height: 300,
    },
    secondaryPicture: {
      alignItems: 'center',
      resizeMode: 'center',
      width: 'auto',
      height: 150,
    },
    welcomePicture: {
      alignItems: 'center',
      resizeMode: 'center',
      width: 'auto',
      height: 500,
    },
    horizontalLayout: {
      flexDirection: 'row',
      justifyContent: 'flex-start',
      margin: 10,
    },
    horizontalLayout2: {
      flexDirection: 'row',
      justifyContent: 'flex-start',
      alignItems: 'stretch',
      margin: 10,
    },
    horizontalLayout3: {
      flexDirection: 'row',
      justifyContent: 'center',       
      margin: 10,     
      color: '#FCF8E8'
    },
    smallText: {
      fontWeight: 'bold',
      fontSize: 28,
      textAlign: 'center',
      color: '#FCF8E8'
    },
    smallText2: {
      fontWeight: 'bold',
      fontSize: 24,
      color: '#FCF8E8'
    },
    smallText3: {
      fontWeight: 'bold',
      fontSize: 20,
      textAlign: 'right',
      color: '#FCF8E8'
    },
    dropdownListText: {
      fontSize: 28,
      color: '#FCF8E8',
    },
    secondText: {
      fontSize: 28,
      color: '#FCF8E8'
    },
    secondText2: {
      fontSize: 20,
      color: '#FCF8E8'
    },
    thirdText: {
      fontSize: 20,    
      margin: 10,
      color: '#FCF8E8'
    },
    infoText: {
      fontSize: 14,
      marginTop: 30,
      textAlign: 'center',
      color: '#FCF8E8'
    },
    infoHistoryText: {
      fontSize: 14,
      textAlign: 'center',
      color: '#FCF8E8'
    },
    infoGenreText: {
      fontSize: 14,
      textAlign: 'center',
      color: '#FCF8E8'
    },
    colorHistoryText: {
      color: '#FCF8E8'
    },
    textInputMod: {
      fontSize: 28,
      marginLeft: 5,
    },
    // Button customization and information regarding the OnPress expression:
    // Author: Expo (n.d.)
    // Link: https://docs.expo.dev/ui-programming/react-native-styling-buttons/
    buttonMod: {
      alignSelf: 'center',
      margin: 15,
      width: 250,
    },
    buttonMod2: {
      margin: 10,
      width: 100,
    },
    buttonMod3: {
      margin: 10,
      width: 120,
    },
    buttonMod4: {
      width: 100,
    },
    buttonModLeft: {
      width: 100,
      marginLeft: 10,
    },
  });

  export default styles;