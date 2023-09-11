import React, { useEffect } from "react";
import { Link, useNavigate, useParams } from "react-router-dom";
import { Row, Col, ListGroup, Image, Button } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import Message from "../components/Message.jsx";
import Loader from "../components/Loader.jsx";
import { getOrderDetails } from "../actions/orderActions.jsx";

function OrderScreen() {
  const { orderId } = useParams();

  const dispatch = useDispatch();

  const orderDetails = useSelector((state) => state.orderDetails);
  const { order, loading, error } = orderDetails;

  if (!loading && !error) {
    order.itemsPrice = order.order_items
      .reduce((acc, item) => acc + item.price * item.quantity, 0)
      .toFixed(2);
  }

  useEffect(() => {
    console.log("UseEffect");
    if (!order || order.id !== Number(orderId)) {
      dispatch(getOrderDetails(orderId));
    }
  }, [dispatch, orderId, order]);

  if (order) {
    return loading ? (
      <Loader />
    ) : error ? (
      <Message variant="danger">{error}</Message>
    ) : (
      <div>
        <h1>Order: {order.id}</h1>
        <Row>
          <Col md={8}>
            <ListGroup variant="flush">
              <ListGroup.Item>
                <h2>Shipping</h2>

                <p>
                  <strong>Name: </strong> {order.user.name}
                </p>
                <p>
                  <strong>Email: </strong>{" "}
                  <a href={`mailto: ${order.user.email}`}>{order.user.email}</a>
                </p>

                {order.is_delivered ? (
                  <Message variant="success">
                    Delivered on {order.paid_at}
                  </Message>
                ) : (
                  <Message variant="warning">
                    Not Delivered {order.paid_at}
                  </Message>
                )}

                <p>
                  <strong>Shipping: </strong>
                  {order.shipping_address.address},{" "}
                  {order.shipping_address.city}
                  {"   "}
                  {order.shipping_address.postalCode},{"   "}
                  {order.shipping_address.country}
                </p>
              </ListGroup.Item>

              <ListGroup.Item>
                <h2>Payment Method</h2>

                <p>
                  <strong>Payment Method: </strong>
                  {order.payment_method}
                </p>

                {order.is_paid ? (
                  <Message variant="success">Paid on {order.paid_at}</Message>
                ) : (
                  <Message variant="warning">Not Paid {order.paid_at}</Message>
                )}
              </ListGroup.Item>

              <ListGroup.Item>
                <h2>Order Items</h2>

                {!order.order_items ? (
                  <Message variant="info">Order is empty</Message>
                ) : (
                  <ListGroup variant="flush">
                    {order.order_items.map((item, index) => (
                      <ListGroup.Item key={index}>
                        <Row>
                          <Col md={1}>
                            <Image
                              src={item.image}
                              alt={item.name}
                              fluid
                              rounded
                            />
                          </Col>

                          <Col>
                            <Link to={`/products/${item.id}`}>{item.name}</Link>
                          </Col>

                          <Col>
                            {item.quantity} X ${item.price} ={" "}
                            {(item.quantity * item.price).toFixed(2)}
                          </Col>
                        </Row>
                      </ListGroup.Item>
                    ))}
                  </ListGroup>
                )}
              </ListGroup.Item>
            </ListGroup>
          </Col>

          <Col md={4}>
            <ListGroup>
              <ListGroup.Item>
                <h2>Order Summery</h2>
              </ListGroup.Item>

              <ListGroup.Item>
                <Row>
                  <Col>Items:</Col>
                  <Col>${order.itemsPrice}</Col>
                </Row>
              </ListGroup.Item>

              <ListGroup.Item>
                <Row>
                  <Col>Shipping:</Col>
                  <Col>${order.shipping_price}</Col>
                </Row>
              </ListGroup.Item>

              <ListGroup.Item>
                <Row>
                  <Col>Tax:</Col>
                  <Col>${order.tax_price}</Col>
                </Row>
              </ListGroup.Item>

              <ListGroup.Item>
                <Row>
                  <Col>Total:</Col>
                  <Col>${order.total_price}</Col>
                </Row>
              </ListGroup.Item>
            </ListGroup>
          </Col>
        </Row>
      </div>
    );
  }
}

export default OrderScreen;
