import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet, ScrollView } from 'react-native';

const primaryColor = '#674a99';

const ProfileScreen = () => {
  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <View style={styles.profilePicContainer}>
          <Text style={styles.profilePic}>👤</Text>
        </View>
        <Text style={styles.username}>Username</Text>
      </View>

      <ScrollView style={styles.optionsContainer}>
        <TouchableOpacity style={styles.option}>
          <Text style={styles.optionText}>Edit Profile</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.option}>
          <Text style={styles.optionText}>Change Password</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.option}>
          <Text style={styles.optionText}>Privacy Settings</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.option}>
          <Text style={styles.optionText}>Notifications</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.option}>
          <Text style={styles.optionText}>Account Settings</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.option}>
          <Text style={styles.optionText}>Help Center</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.option}>
          <Text style={styles.optionText}>Log Out</Text>
        </TouchableOpacity>
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff', padding: 25, paddingTop: 60 },
  header: { alignItems: 'center', marginBottom: 25 },
  profilePicContainer: { width: 100, height: 100, borderRadius: 50, backgroundColor: '#f4f4f4', justifyContent: 'center', alignItems: 'center', marginBottom: 10 },
  profilePic: { fontSize: 40, color: primaryColor },
  username: { fontSize: 22, fontWeight: 'bold', color: '#333' },
  optionsContainer: { marginTop: 20 },
  option: { paddingVertical: 16, borderBottomWidth: 1, borderBottomColor: '#ddd', borderRadius: 8, marginBottom: 12, backgroundColor: '#f9f9f9' },
  optionText: { fontSize: 18, color: primaryColor, textAlign: 'center' },
});


export default ProfileScreen;
