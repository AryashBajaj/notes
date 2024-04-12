import react from "react";
import {BrowserRouter, Routes, Route, Navigate} from "react-router-dom";
import Login from "./pages/Login";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";
import Register from "./pages/Register";
import ProtectedRoute from "./components/ProtectedRoutes";

function Logout() {
  localStorage.clear();
  return <Navigate to="/login"></Navigate>
}

function RegisterAndLogout() {
  localStorage.clear();
  return <Register></Register>;
}


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route 
        path="/"
        element={
          <ProtectedRoute>
            <Home></Home>
          </ProtectedRoute>
        }
        />
        <Route path="/login/" element={ <Login></Login> }/>
        <Route path="/logout/" element={ <Logout></Logout> }/>
        <Route path="/register/" element={ <RegisterAndLogout></RegisterAndLogout> }/>
        <Route path="*" element={ <NotFound></NotFound> }/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;