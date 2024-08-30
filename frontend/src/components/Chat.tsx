import React, { useState } from 'react';
import axios from 'axios';

interface Message {
  text: string;
  sender: string;
}

const Chat: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');

  const sendMessage = async () => {
    if (input.trim()) {
      const userMessage: Message = { text: input, sender: 'user' };
      setMessages([...messages, userMessage]);

      try {
        const response = await axios.post('http://localhost:4000/chat', { message: input });
        console.log('respnsefrent>>>>>>>>>>>>>>', response.data)
        const botMessage: Message = { text: response.data.response, sender: 'bot' };
        setMessages([...messages, userMessage, botMessage]);
      } catch (error) {
        console.error("Error sending message", error);
      }

      setInput('');
    }
  };

  return (
    <div>
      <div className="chat-window">
        {messages.map((msg, index) => (
          <div key={index} className={msg.sender === 'user' ? 'user-message' : 'bot-message'}>
            {msg.text}
          </div>
        ))}
      </div>
      <div className="input-area">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your message..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chat;
