import { Container } from "react-bootstrap";
import {
  createBrowserRouter,
  createRoutesFromElements,
  RouterProvider,
  Route,
  Outlet,
} from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";

import HomeScreen from "./screens/HomeScreen";
import ProductScreen from "./screens/ProductScreen";
import CartScreen from "./screens/CartScreen";
import LoginScreen from "./screens/LoginScreen";
import RegisterScreen from "./screens/RegisterScreen";
import ProfileScreen from "./screens/ProfileScreen";

const Root = () => {
  return (
    <div>
      <Header />
      <main className="py-3">
        <Container>
          <Outlet />
        </Container>
      </main>
      <Footer />
    </div>
  );
};

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<Root />}>
      <Route index element={<HomeScreen />} />
      <Route
        path="/register"
        element={<RegisterScreen />}
      />
      <Route
        path="/login"
        element={<LoginScreen />}
      />
      <Route
        path="/profile"
        element={<ProfileScreen />}
      />
      <Route
        path="/products/:productId"
        element={<ProductScreen />}
      />
      <Route
        path="/cart/:productId?"
        element={<CartScreen />}
      />
    </Route>
  )
);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
