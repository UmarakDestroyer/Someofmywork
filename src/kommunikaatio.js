import axios from "axios"
const baseUrl="http://localhost:3001/persons"

const kaikki =()=>{
    const request = axios.get(baseUrl);
    return request.then(r=>r.data)
}

const lisaa = (object)=>{
    const request = axios.post(baseUrl, object);
    return request.then(r=>r.data)
}

const poista = (nimi)=>{
    const request = axios.delete(`${baseUrl}/${nimi}`);
    return request.then(r=>r.data)
}
const muokkaa = (uusi, id)=>{
    const request = axios.put(`${baseUrl}/${id}`, uusi);
    return request.then(r=>r.data)
}

export default {kaikki, lisaa,poista,muokkaa}