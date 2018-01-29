<template>
  <div id="app">
    <img src="./assets/logo.png">
    {{ restData }}
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "app",
  data() {
    return {
      restData: axios.get("http://localhost:5000").then(function(res) {
        return res;
      })
    };
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
  margin-top: 60px;
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
