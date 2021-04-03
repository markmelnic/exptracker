<template>
  <div id="app">
    <People v-bind:people="people"/>
  </div>
</template>

<script>
import axios from 'axios';

import People from './components/People'

export default {
  name: 'App',
  components: {
    People
  },
  data() {
    return {
      people: [
        {
          id: 1,
          name: "Mark",
          share: 50
        },
        {
          id: 2,
          name: "Traian",
          share: 50
        }
      ],
      msg: '',
    }
  },
    methods: {
    getMessage() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
          console.log(this.msg);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

<style>
#app {
  font-family: Montserrat;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#app::-webkit-scrollbar {
  display: none;
}
</style>
