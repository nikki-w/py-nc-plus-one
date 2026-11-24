import { BrowserRouter } from 'react-router';
import './App.css'
import AppRoutes from './AppRoutes'


function App() {

  return (
    <BrowserRouter>
      <AppRoutes/>
    </BrowserRouter>
  )
}

export default App;
