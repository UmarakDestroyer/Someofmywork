import {useState, useEffect} from 'react'
import commy from "./kommunikaatio"
import axios from "axios"

const Filter = (props) => {

    return (
        <div>filter shown with:
            <input value={props.filterWord}
                onChange={
                    props.handleFilterChange
                }/></div>
    )
}
const Notification = ({ message }) => {
    if (message === null) {
      return null
    }
   const messagestyle={
        color:"green",
        fontStyle:"italic",
        fontSize: 40,
        borderWidth:5,
        borderColor:"green",
        borderStyle:"solid",
        padding:10
    }
    return (
      <div style={messagestyle}>
        {message}
      </div>
    )
  }

const PersonForm = (props) => {
    return (
        <form>
            <div>
                name:
                <input value={props.newName}
                    onChange={
                       props.handleNameChange
                    }/>
            </div>
        <div>
            number:
            <input value={props.newNumber}
                onChange={
                    props.handleNumberChange
                }/>
        </div>
    <div>
        <button type="submit"
            onClick={
                (event) => {
                    event.preventDefault();
                   const sama = props.persons.find(alkio => alkio.name === props.newName);
                   console.log(sama)
                    if (sama) {
                        if(window.confirm(`${props.newName} has already added to phone book, replace old number with the new one?`)){
                   
                            commy.muokkaa({name:props.newName, number:props.newNumber}, sama.id).then(r=>{props.changePersons({nimi:props.newName, number:props.newNumber});props.changeMessage(`${props.newName} number has been changed to ${props.newNumber}`);
                            setTimeout(() => {  props.changeMessage(null) }, 1000)}).catch(
                                error=>{
                                props.changeMessage(`${props.newName} has already been removed from the server`);
                                setTimeout(() => {  props.changeMessage(null) }, 1000)}
                            );
                            
                            return

                        };
                        
                    }
  
                    commy.lisaa({name: props.newName, number: props.newNumber} ).then(r=> props.handlePersonChange(props.persons.concat(r)));
                    props.changeMessage(`${props.newName} has been added`)
                    setTimeout(() => {  props.changeMessage(null) }, 1000)

                }
        }>add</button>
    </div>
</form>
    )
}
const poistaa =(r,s, k)=>{
    if(window.confirm(`${s} will be deleted`)){
        commy.poista(r).then(p=>p);
        k(r);

    }
    

}
const Persons =(props)=>{
    console.log(props.nimi.name)
    return(<div><p key={props.nimi.id}>
        {props.nimi.name}  {props.nimi.number}</p>
    <button onClick={()=>{poistaa(props.nimi.id, props.nimi.name, props.poista)}}>delete</button> </div>)
}




const Person = (props) => {
    const filter = props.filterWord;
    console.log(props.person)
    if(filter==""){
        return( props.persons.map(nimi=> <Persons nimi={nimi}  poista={props.deleteFrom} /> ) )
    };
    return(props.persons.filter(person => person.name.toLowerCase().includes(filter.toLowerCase())).map(nimi => <Persons nimi={nimi} poista={props.deleteFrom} />))
}

const App = () => {
    const [persons, setPersons] = useState([])
    const [newName, setNewName] = useState('')
    const [newNumber, setNewNumber] = useState("")
    const [filterWord, setFilter] = useState("")
    const [message, setMessage] =useState(null)

    const handleFilterChange =(event) => {
      setFilter(event.target.value)
    }
    const handleNameChange= (event)=> {
      setNewName(event.target.value)
    }
    const handleNumberChange = (event)=>{
      setNewNumber(event.target.value)
    }
    const handlePersonChange = (uusi) =>{
      setPersons(uusi)
    }
    const deleteFrom=(uusi)=>{
        setPersons(persons.filter((person)=> person.id!=uusi))
    }
    const changePersons=(uusi)=>{
        const i  = persons.indexOf(persons.find(a=>a.name===uusi.name))
        const Copy = [...persons]
        Copy[i].number=uusi.number
        Copy[i].name= persons[i].name
        Copy[i].id = persons[i].id
        setPersons(Copy)
    }
    
    const changeMessage=(a)=>{
        setMessage(a)

    }
    
    useEffect(()=>{
    commy.kaikki().then(r=>setPersons(r));
   

    }, [])
    return (
        <div>
            <Notification message = {message}/>
            <h2>Phonebook</h2>
            <Filter filterWord={filterWord} handleFilterChange={handleFilterChange} />
            
                <h2>Add new</h2>
            <PersonForm changeMessage={changeMessage} newName={newName} handleNameChange={handleNameChange} changePersons={changePersons} handlePersonChange={handlePersonChange} persons={persons} newNumber={newNumber} handleNumberChange={handleNumberChange}  />

            
            <h2>Numbers</h2>
            <Person persons={persons} filterWord={filterWord} deleteFrom={deleteFrom}/>
        </div>
    )

}

export default App
