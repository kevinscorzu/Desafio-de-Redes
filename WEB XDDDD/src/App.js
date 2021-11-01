import styled from "styled-components";
import "./App.css";
import { useState } from "react";
import {
  CircleLoader,
  ClipLoader,
  DotLoader,
  SyncLoader,
} from "react-spinners";

const Box = styled.div`
  background-color: #e9e6ff;
  max-width: 1024px;
  margin: 16px auto;
  padding: 16px;
  display: flex;
  flex-direction: column;
`;

const Input = styled.div`
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 20px;
  border-bottom: 1px solid #ccc;
  padding: 8px;
  margin-bottom: 16px;
  select,
  button,
  input {
    padding: 8px;
    font-size: 16px;
    cursor: pointer;
  }

  img {
    width: 80%;
    border: 1px solid #ccc;
    border-radius: 8px;
  }
`;

const FILTERS = ["f1", "f2", "f3"];

function App() {
  const [filter, setFilter] = useState(FILTERS[0]);
  const [image, setImage] = useState(null);
  const [loading, setLoading] = useState(false);

  const upload = () => {
    alert(JSON.stringify({ image, filter }));
    setLoading(true);
  };

  return (
    <div className="App">
      <Box>
        <h1>Filtro de imágenes online</h1>
        <div>
          <Input>
            <p>1. Seleccione el tipo de filtrado</p>
            <select value={filter} onChange={(e) => setFilter(e.target.value)}>
              {FILTERS.map((el) => (
                <option>{el}</option>
              ))}
            </select>
          </Input>
          <Input>
            <p>2. Seleccione la imagen</p>
            <input
              onChange={(e) => setImage(e.target.files[0])}
              type="file"
              id="img"
              name="img"
              accept="image/*"
            />
            {image && (
              <img src={URL.createObjectURL(image)} alt="preview"></img>
            )}
          </Input>
          <Input>
            <p>3. Verifique la imagen e inicie el proceso</p>
            {!loading ? (
              <button onClick={upload}>
                Iniciar el procesamiento de la imagen
              </button>
            ) : (
              <SyncLoader />
            )}
          </Input>
        </div>
      </Box>
    </div>
  );
}

export default App;
