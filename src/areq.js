import axios from 'axios'
axios.defaults.baseURL = process.env.VUE_APP_API_URL

async function areq(path) {
    return await axios.get(axios.defaults.baseURL + path)
    .then(response => response.data)
    .catch(error => console.log(error));
}

export default areq
