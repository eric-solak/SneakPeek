import React from 'react';
import { View, Text, Image, StyleSheet } from 'react-native';

const IP = `${process.env.EXPO_PUBLIC_IP}`;
const primaryColor = '#674a99';

const PostDetailScreen = ({ route }) => {
  const { post } = route.params;

  return (
    <View style={styles.container}>
        <View style={styles.postContainer}>
            <Text style={styles.heading}>{post.title}</Text>
            <Image
            source={{ uri: `http://${IP}:5000/${post.image_path}` }}
            style={styles.image}
            resizeMode="cover"
            />
            <Text style={styles.description}>{post.description}</Text>
            <Text style={styles.rating}>⭐ {post.rating}</Text>
        </View>

        <View style={styles.separator} />

        <View style={styles.moderatorCommentContainer}>
            <Text style={styles.moderatorName}>Identifier Bot:</Text>
            <Text style={styles.moderatorComment}>{post.identification}</Text>
        </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  image: { width: '100%', height: 250 },
  description: { fontSize: 16, padding: 12, color: '#333' },
  heading: {fontSize: 24, fontWeight: 'bold', color: '#333', paddingVertical: 6, paddingHorizontal: 12},
  rating: { fontSize: 16, fontWeight: 'bold', paddingLeft: 12, color: primaryColor },
  separator: {height: 1, backgroundColor: '#ccc', marginVertical: 12}, 
  moderatorCommentContainer: {paddingVertical: 12, paddingHorizontal: 16, backgroundColor: '#f7f7f7', borderRadius: 8, marginBottom: 12},
  moderatorName: {fontSize: 16, fontWeight: 'bold', color: '#674a99', marginBottom: 6},
  moderatorComment: {fontSize: 14, color: '#333'},
});

export default PostDetailScreen;
