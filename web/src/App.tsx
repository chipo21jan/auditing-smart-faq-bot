import React, { useState } from 'react';
import './App.css';

interface Message {
  role: 'user' | 'assistant';
  content: string;
  citations?: Citation[];
}

interface Citation {
  content: string;
  location: any;
  metadata: any;
}

function App() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [sessionId] = useState(() => `session-${Date.now()}`);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage: Message = { role: 'user', content: input };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      // API Gateway endpoint
      const response = await fetch('https://p7z41veq9l.execute-api.us-east-1.amazonaws.com/prod/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          question: input,
          session_id: sessionId
        })
      });

      const data = await response.json();
      
      const assistantMessage: Message = {
        role: 'assistant',
        content: data.answer,
        citations: data.citations
      };
      
      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      console.error('Error:', error);
      setMessages(prev => [...prev, {
        role: 'assistant',
        content: 'Sorry, an error occurred. Please try again.'
      }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="header">
        <h1>Auditing Smart FAQ Bot</h1>
        <p>Ask questions about policies, SOPs, donor rules, and audit reports</p>
      </header>

      <div className="chat-container">
        <div className="messages">
          {messages.map((msg, idx) => (
            <div key={idx} className={`message ${msg.role}`}>
              <div className="message-content">{msg.content}</div>
              {msg.citations && msg.citations.length > 0 && (
                <div className="citations">
                  <strong>Sources:</strong>
                  {msg.citations.map((cite, i) => (
                    <div key={i} className="citation">
                      <small>
                        {cite.location?.s3Location?.uri || 'Document'} - 
                        {cite.metadata?.['x-amz-bedrock-kb-chunk-id'] || `Chunk ${i + 1}`}
                      </small>
                    </div>
                  ))}
                </div>
              )}
            </div>
          ))}
          {loading && <div className="message assistant loading">Thinking...</div>}
        </div>

        <div className="input-container">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
            placeholder="Ask a question..."
            disabled={loading}
          />
          <button onClick={sendMessage} disabled={loading || !input.trim()}>
            Send
          </button>
        </div>
      </div>

      <div className="examples">
        <h3>Example Questions:</h3>
        <ul>
          <li>What is the procurement threshold for competitive bidding?</li>
          <li>What evidence is required for travel expense verification?</li>
          <li>Show me segregation of duties requirements for cash handling</li>
          <li>What characterizes an acceptable gift given to an employee?</li>
        </ul>
      </div>
    </div>
  );
}

export default App;
