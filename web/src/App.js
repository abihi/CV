import React from 'react'
import { Route, Switch } from 'react-router-dom'
import ProfilePage from './pages/ProfilePage'

export default function App() {
  return (
    <Switch>
      <Route exact path="/" component={ProfilePage} />
    </Switch>
  )
}