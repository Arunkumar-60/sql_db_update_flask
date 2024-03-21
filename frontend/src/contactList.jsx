import react from "react"

const ContactList = ({contacts, updateContact ,updateCallBack}) => {
    const onDelete = async(id) => {
        try {
            const options = {
                method: "DELETE"
            }
            const response = await fetch(`http://127.0.0.1:5000/delete_contact/${id}`, options)
            if (response.status === 200) {
                updateCallBack()
            }
            else{
                console.error("failed to delete")

            }
        }
        catch (error){
            alert(error)
        }
    }

    return <div className="table-responsive"><br />
        <h1 class="d-flex justify-content-center">list of contacts</h1>
        
        <table class="table table-dark table-striped">
            <thead class="table-light">
                <tr>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Email</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {contacts.map((contact)=>(
                    <tr key={contact.id}>
                        <td>{contact.firstName}</td>
                        <td>{contact.lastName}</td>
                        <td>{contact.email}</td>
                        <td>
                            <button onClick={() => updateContact(contact)}>Update</button>
                            <button onClick={()=> onDelete(contact.id)}>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
}

export default ContactList