import { useState } from 'react';
import { Chessboard } from 'react-chessboard';
import { Chess } from 'chess.js';
import FirebaseConnector from '../firebase';

const ChessUI = () => {
    //const [game, setGame] = useState(new Chess());








    return (
        <div>
            <h1>ChessUI</h1>
            <Chessboard
                width={400}
                height={400}
                position={"start"} />
        </div>
    );
};
export default ChessUI