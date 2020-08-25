import React, { useState, useEffect } from 'react'
import axios from 'axios'

export default function ProfilePage(props) {
  // Setting initial state
  const initialprofileState = {
    profile: {},
    loading: true,
  }

  // Getter and setter for profile state
  const [profile, setprofile] = useState(initialprofileState)

  // Using useEffect to retrieve data from an API
  useEffect(() => {
    const getprofile = async () => {
      const { data } = await axios(
        `http://127.0.0.1:8000/profiles/1`
      )

      // Update state
      setprofile(data)
    }
    
    getprofile()
  }, []) // Don't forget the `[]`, which will prevent useEffect from running in an infinite loop

  return profile.loading ? (
    <div>Loading...</div>
  ) : (
    <div className="container">
      <h1>{profile.id}</h1>

      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
            <th>Address</th>
            <th>Birthdate</th>
            <th>About me</th>
            <th>Telephone number</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{profile.name}</td>
            <td>{profile.email}</td>
            <td>{profile.address}</td>
            <td>{profile.birthdate}</td>
            <td>{profile.about_me}</td>
            <td>{profile.telephone_number}</td>
          </tr>
        </tbody>
      </table>
    </div>
  )
}