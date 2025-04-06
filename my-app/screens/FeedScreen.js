import React, { useEffect, useState } from 'react';
import { useNavigation } from '@react-navigation/native';
import { StyleSheet, Text, View, FlatList, Image, TouchableOpacity } from 'react-native';

const IP = `${process.env.EXPO_PUBLIC_IP}`;
const primaryColor = '#674a99';

const FeedScreen = () => {
  const [posts, setPosts] = useState([]);
  const API_URL = `http://${IP}:5000/get-posts`;
  const navigation = useNavigation();

  useEffect(() => {
    fetch(API_URL)
      .then((res) => res.json())
      .then((data) => {
        setPosts(data.posts);
      })
      .catch((error) => {
        console.error("Error fetching posts:", error);
      });
  }, []);

  const renderItem = ({ item }) => (
    <TouchableOpacity onPress={() => navigation.navigate('PostDetail', { post: item })}>
      <View style={styles.postContainer}>
        <Image
          source={{ uri: `http://${IP}:5000/${item.image_path}` }}
          style={styles.image}
          resizeMode="cover"
        />
        <Text style={styles.description}>{item.description}</Text>
        <Text style={styles.rating}>⭐ {item.rating}</Text>
      </View>
    </TouchableOpacity>
  );

  return (
    <View style={styles.container}>
      <FlatList
        data={posts}
        keyExtractor={(item) => item.pid.toString()}
        renderItem={renderItem}
        contentContainerStyle={styles.list}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  list: {
    padding: 16,
  },
  postContainer: {
    marginBottom: 20,
    borderRadius: 10,
    backgroundColor: '#f4f4f4',
    padding: 12,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowRadius: 4,
    elevation: 2,
  },
  image: {
    width: '100%',
    height: 200,
    borderRadius: 10,
    marginBottom: 10,
  },
  description: {
    fontSize: 16,
    color: '#333',
    marginBottom: 4,
  },
  rating: {
    fontSize: 14,
    color: primaryColor,
    fontWeight: 'bold',
  },
});

export default FeedScreen;
