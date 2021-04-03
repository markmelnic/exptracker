<template>
    <table>
        <th>
            Person
        </th>
        <th>
            Share
        </th>
    <tr v-bind:key="person.id" v-for="person in people">
        <td>{{person.name}}</td>
        <td>{{person.share}}%</td>
    </tr>
    </table>
</template>

<script>
import axios from 'axios';
axios.defaults.baseURL = process.env.VUE_APP_API_URL

export default {
    name: "People",
    data() {
        return {
            people: null
        }
    },
    methods: {
        getPeople: function(path) {
        return axios.get(axios.defaults.baseURL + path)
        .then(response => response.data)
        .then(people => this.people = people)
        .catch(error => console.log(error))
        },
    },
    created: async function() {
        await this.getPeople('people')
    }

}
</script>

<style scoped lang="scss">
table {
    border: solid 1px black;
    td {
        counter-reset: 2;
    }
}
tr, th, td {
    border: solid 1px black;
}
</style>
