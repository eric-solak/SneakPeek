import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

import LoginScreen from './screens/LoginScreen';
import CreateAccountScreen from './screens/CreateAccountScreen';
import FeedScreen from './screens/FeedScreen';
import CreatePostScreen from './screens/CreatePostScreen';
import ProfileScreen from './screens/ProfileScreen';
import PostDetailScreen from './screens/PostDetailScreen';
import Ionicons from 'react-native-vector-icons/Ionicons';

const Stack = createStackNavigator();
const Tab = createBottomTabNavigator();
const primaryColor = '#674a99';

function MainTabs() {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        headerShown: false,
        tabBarActiveTintColor: primaryColor,
        tabBarInactiveTintColor: 'gray',
        tabBarIcon: ({ color, size }) => {
          let iconName;

          if (route.name === 'Feed') {
            iconName = 'home-outline';
          } else if (route.name === 'Create Post') {
            iconName = 'add-circle-outline';
          } else if (route.name === 'Profile') {
            iconName = 'person-outline';
          }

          return <Ionicons name={iconName} size={size} color={color} />;
        },
      })}
    >
      <Tab.Screen name="Feed" component={FeedScreen} />
      <Tab.Screen name="Create Post" component={CreatePostScreen} />
      <Tab.Screen name="Profile" component={ProfileScreen} />
    </Tab.Navigator>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        initialRouteName="Login"
        screenOptions={{
          headerStyle: { backgroundColor: primaryColor },
          headerTintColor: '#fff',
        }}
      >
        <Stack.Screen name="Login" component={LoginScreen} />
        <Stack.Screen name="CreateAccount" component={CreateAccountScreen} />
        <Stack.Screen name="Main" component={MainTabs} options={{ headerShown: false }} />
        <Stack.Screen name="PostDetail" component={PostDetailScreen} options={{ title: 'Post' }} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
