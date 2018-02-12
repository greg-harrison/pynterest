<template>
  <div id="app">
    <header/>
    {{ restData }}
  </div>
</template>

<script>
import axios from "axios";
import header from "./components/base_components/header";

export default {
  name: "app",
  data: () => ({
    restData: []
  }),
  methods: {
    fetchData() {
      var vm = this;
      axios.get("http://localhost:5000").then(function(res) {
        vm.restData = JSON.stringify(res.data.users);
      });
    }
  },
  created() {
    this.fetchData();
  },
  components: {
    header: header
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
