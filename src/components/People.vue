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

    <input v-model="name" placeholder="Name" required />
    <input v-model="share" placeholder="Share %" required />
    <button @click.prevent="addUser()">Submit Post</button>

</template>

<script>
import { greq, preq } from '@/areq.js';

export default {
    name: "People",
    data() {
        return {
            people: null
        }
    },
    methods: {
        async addUser() {
            this.people = await preq('add_user', {name: this.name, share: this.share})
        }
    },
    created: async function() {
        this.people = await greq('people')
    }
}
</script>

<style scoped lang="scss">
table {
    width: 20em;
    border: solid 1px black;
    td {
        counter-reset: 2;
    }
}
tr, th, td {
    border: solid 1px black;
}
</style>
