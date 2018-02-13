<template>
  <div id="app">
    <Header/>
    <PynContainer/>
  </div>
</template>

<script>
import axios from "axios";
import Header from "./components/base_components/header";
import PynContainer from "./components/base_components/pyn-container";

export default {
  name: "app",
  components: {
    Header,
    PynContainer
  }
};
</script>

<style lang="scss">
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
html,
body {
  width: 100%;
  height: 100%;
  margin: 0;
}

h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
