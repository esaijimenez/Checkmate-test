import { useState } from 'react';
import { Chessboard } from 'react-chessboard';
import { Chess } from 'chess.js';

const ChessUI = () => {
    const [game, setGame] = useState(new Chess());

    return (
        <div>
            <h1>ChessUI</h1>
            <Chessboard position={"start"} />
        </div>
    );
};
export default ChessUI