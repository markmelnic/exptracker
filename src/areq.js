import axios from 'axios'
axios.defaults.baseURL = process.env.VUE_APP_API_URL

async function greq(path) {
    return await axios.get(axios.defaults.baseURL + path)
    .then(response => response.data)
    .catch(error => console.log(error));
}

async function preq(path, data) {
    return await axios.post(axios.defaults.baseURL + path, data)
    .then(response => response.data)
    .catch(error => console.log(error));
}

export { greq, preq }
