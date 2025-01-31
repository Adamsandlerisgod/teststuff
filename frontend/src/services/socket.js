let socket = new WebSocket('ws://localhost:8000/ws/chat/');

const reconnect = () => {
  console.log('Reconnecting...');
  // Attempt to reconnect after 2 seconds
  setTimeout(() => {
    socket = new WebSocket('ws://localhost:8000/ws/chat/');
  }, 2000);
};

socket.onopen = () => {
  console.log('Connected to WebSocket');
};

socket.onerror = (error) => {
  console.error('WebSocket error:', error);
  reconnect();
};

socket.onclose = (event) => {
  console.log('WebSocket closed:', event);
  reconnect();
};

export const sendMessage = (message) => {
  if (socket.readyState === WebSocket.OPEN) {
    socket.send(JSON.stringify({ message }));
  } else {
    console.error('WebSocket is not open');
  }
};

export const onMessage = (callback) => {
  socket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    callback(data);
  };
};
