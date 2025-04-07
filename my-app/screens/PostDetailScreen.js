import { React, useState, useEffect } from 'react';
import {
  View,
  Text,
  Image,
  StyleSheet,
  FlatList,
  TextInput,
  Button,
  Alert,
  KeyboardAvoidingView,
  Platform,
  ScrollView
} from 'react-native';


const IP = `${process.env.EXPO_PUBLIC_IP}`;
const primaryColor = '#674a99';

const PostDetailScreen = ({ route }) => {
  const { post } = route.params;
  const [comments, setComments] = useState([]); 
  const [newComment, setNewComment] = useState('');

  useEffect(() => {
    fetchComments();
  }, [post.pid]); 

  const fetchComments = () => {
    fetch(`http://${IP}:5000/get-comments?pid=${post.pid}`)
      .then((response) => response.json())
      .then((data) => {
        setComments(data.comments); 
      })
      .catch((error) => {
        console.error('Error fetching comments:', error);
      });
  };

  const handleAddComment = () => {
    if (newComment.trim() === '') {
      Alert.alert('Please enter a comment before submitting.');
      return;
    }

    fetch(`http://${IP}:5000/add-comment`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ pid: post.pid, body: newComment }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          setNewComment('');
          fetchComments(); // refresh comment list
        } else {
          Alert.alert('Error', 'Failed to add comment.');
        }
      })
      .catch((error) => {
        console.error('Error adding comment:', error);
      });
  };

  const renderComment = ({ item }) => (
    <View style={styles.commentContainer}>
      <Text style={styles.commentText}>{item.body}</Text>
    </View>
  );

  return (
    <KeyboardAvoidingView
      style={{ flex: 1 }}
      behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
      keyboardVerticalOffset={80}
    >
      <View style={styles.container}>
        <FlatList
          data={comments}
          keyExtractor={(item) => item.cid.toString()}
          renderItem={renderComment}
          contentContainerStyle={styles.commentList}
          ListHeaderComponent={
            <>
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
  
              {post.identification && (
                <View style={styles.moderatorCommentContainer}>
                  <Text style={styles.moderatorName}>Identifier Bot:</Text>
                  <Text style={styles.moderatorComment}>
                    These shoes are: <Text style={{ fontWeight: 'bold' }}>{post.identification}</Text>
                  </Text>
                  <Text style={styles.moderatorComment}>
                    They can be bought at: <Text style={{ fontWeight: 'bold' }}>{post.link}</Text>
                  </Text>
                </View>
              )}
  
              <Text style={styles.commentsHeading}>Comments:</Text>
            </>
          }
          ListFooterComponent={
            <View style={styles.commentInputRow}>
              <TextInput
                style={styles.commentInput}
                placeholder="Add a comment..."
                value={newComment}
                onChangeText={setNewComment}
              />
              <Button title="Send" onPress={handleAddComment} color={primaryColor} />
            </View>
          }
          keyboardShouldPersistTaps="handled"
        />
      </View>
    </KeyboardAvoidingView>
  );  
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff' },
  postContainer: { paddingBottom: 12 },
  image: { width: '100%', height: 250 },
  description: { fontSize: 16, padding: 12, color: '#333' },
  heading: { fontSize: 24, fontWeight: 'bold', color: '#333', paddingVertical: 6, paddingHorizontal: 12 },
  rating: { fontSize: 16, fontWeight: 'bold', paddingLeft: 12, color: primaryColor },
  separator: { height: 1, backgroundColor: '#ccc', marginVertical: 12 },

  moderatorCommentContainer: { paddingVertical: 12, paddingHorizontal: 16, backgroundColor: '#f7f7f7', borderRadius: 8, marginBottom: 12 },
  moderatorName: { fontSize: 16, fontWeight: 'bold', color: '#674a99', marginBottom: 6 },
  moderatorComment: { fontSize: 14, color: '#333' },

  commentsContainer: { paddingHorizontal: 12, marginBottom: 20 },
  commentsHeading: { fontSize: 18, fontWeight: 'bold', marginBottom: 10, paddingHorizontal: 12 },
  commentList: { paddingBottom: 12 },
  commentContainer: { padding: 10, marginBottom: 10, backgroundColor: '#f0f0f0', borderRadius: 6 },
  commentText: { fontSize: 14, color: '#333', paddingHorizontal: 10 },

  input: { borderColor: '#ccc', borderWidth: 1, padding: 10, borderRadius: 6, marginBottom: 10, fontSize: 14, backgroundColor: '#fafafa' },
  commentInputRow: { flexDirection: 'row', alignItems: 'center', marginBottom: 12, paddingHorizontal: 12 },
  commentInput: { flex: 1, borderColor: '#ccc', borderWidth: 1, padding: 10, borderRadius: 6, fontSize: 14, backgroundColor: '#fafafa', marginRight: 8 },
});

export default PostDetailScreen;
