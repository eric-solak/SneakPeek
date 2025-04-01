import React from 'react';
import { StyleSheet, Text, View } from 'react-native';

const primaryColor = '#674a99';

const FeedScreen = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.feedText}>FEED</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  feedText: {
    fontSize: 32,
    fontWeight: 'bold',
    color: primaryColor,
  },
});

export default FeedScreen;
