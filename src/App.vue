<template>
  <div id="app">
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <h1 id='title'>Django VueJs</h1>
    <!--
    <div id="nav">
     <router-link :to="{ name: 'home' }">Vue</router-link> |
     <router-link :to="{ name: 'messages' }">Django Rest</router-link>
    </div>
  -->
    <router-view></router-view>
  </div>
</template>

<style>
#title {
  font-size: 100px;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
