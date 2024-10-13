import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

axios.defaults.baseURL = 'http://127.0.0.1:5000';

const App = () => {
  const [board, setBoard] = useState([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]);
  const [player, setPlayer] = useState('X');
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get('/board').then(response => {
      setBoard(response.data);
    });
  }, []);

  const handleClick = (row, col) => {
    axios.post('/move', { row, col }).then(response => {
      const data = response.data;
      if (data.status === 'error') {
        setMessage(data.message);
      } else {
        setMessage('');
        axios.get('/board').then(response => {
          setBoard(response.data);
          if (data.status === 'win') {
            setMessage(`Player ${player} wins!`);
          } else if (data.status === 'draw') {
            setMessage('It\'s a draw!');
          } else {
            setPlayer(data.player);
          }
        });
      }
    });
  };

  const handleReset = () => {
    axios.post('/reset').then(response => {
      if (response.data.status === 'reset') {
        setBoard([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]);
        setPlayer('X');
        setMessage('');
      }
    });
  };

  return (
    <div className="App">
      <h1>Tic Tac Toe</h1>
      <div className="board">
        {board.map((row, rowIndex) => (
          <div key={rowIndex} className="row">
            {row.map((cell, colIndex) => (
              <div
                key={colIndex}
                className="cell"
                onClick={() => handleClick(rowIndex, colIndex)}
              >
                {cell}
              </div>
            ))}
          </div>
        ))}
      </div>
      {message && <p>{message}</p>}
      {(message === `Player ${player} wins!` || message === 'It\'s a draw!') && (
        <button onClick={handleReset}>Play Again</button>
      )}
    </div>
  );
};

export default App;
