import React, { useRef, useEffect} from 'react';
import {
  Animated,
} from 'react-native';


const FadeInView = (props) => {
    const fadeAnim = useRef(new Animated.Value(0)).current
  
    useEffect(() => {
      Animated.timing(
        fadeAnim,
        {
          toValue: 1,
          duration: 3000,
          useNativeDriver: false,
        }
      ).start();
    }, [fadeAnim])
  
    return (
      <Animated.View style={{
        ...props.styles,
        opacity: fadeAnim,
      }}>
        {props.children}
      </Animated.View>
    );
  }
  
  // FadeinView was also looked at for examples on how to connect into the welcome screen:
  // Author: Meta Platforms, Inc. 2022
  // Link: https://reactnative.dev/docs/0.66/animations

  export default FadeInView;