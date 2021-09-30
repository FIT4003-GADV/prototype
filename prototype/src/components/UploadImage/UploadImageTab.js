import {Card, CardContent, FormLabel, List} from '@mui/material';
import React, {useState} from 'react';
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";
import {styled} from "@mui/material/styles";
import ListItem from "@mui/material/ListItem";
import IconButton from "@mui/material/IconButton";
import DeleteIcon from '@mui/icons-material/Delete';
import axios from "axios";

const UploadImageTab = () => {
  const [files, setFiles] = useState({files: [], errors: []})

  //If a space or enter, call function
  const keyboardClick = func => e => e.keyCode === 13 || e.keyCode === 32 ? func : false

  const fileInput = React.createRef();

  const handleFileSelect = (uploaded) => {
    if (uploaded.length === 0) {
      //error wrong number of files
      return;
    }
    const validated = []
    const errors = []
    for (let file of uploaded) {
      if (file.type !== "image/svg+xml") {
        errors.push({file: file, error: "Incorrect File Type"})
      } else {
        validated.push(file)
      }
    }
    setFiles({files: [...files.files, ...validated], errors: errors})
  }

  const deleteFile = entry => {
    files.files.splice(entry, 1)
    setFiles({files: files.files, errors: []})
  }

  const uploadFiles = () => {
    for (const file of files.files) {
      axios.request({
        method: "post",
        url: "https://httpbin.org/post",
        data: file,
        onUploadProgress: (p) => {
          console.log(p);
          //this.setState({
          //fileprogress: p.loaded / p.total
          //})
        }
      }).then(data => {
        //this.setState({
        //fileprogress: 1.0,
        //})
      })
    }
  }

  const FileLabel = styled('label')`` // these `` are needed
  return (
      <Card>
        <CardContent>
          <Stack>
            {/*File Input. We hide the input and use the label as a psudeo button*/}
            <FileLabel sx={{
              border: theme => `2px dashed ${theme.palette.primary.main}`,
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              height: theme => theme.spacing(10),
              outline: 'none',
              width: '100%',
              marginBottom: "10px",
              "&:focus": {
                backgroundColor: "#E8E8E8"
              }
            }} htmlFor="fileInput" tabIndex={0}
                       onKeyPress={keyboardClick(() => document.getElementById("fileInput").click())}>
              Drag 'n' drop SVG image here, or click to select image
              <input ref={fileInput} style={{display: "none"}} id="fileInput" type="file"
                     onChange={() => handleFileSelect(Array.from(fileInput.current.files))} multiple/>
            </FileLabel>
            {/*Errors*/}
            <List>
              {
                files.errors.map(error => (
                    <ListItem>
                      <FormLabel error>Failed to upload {error.file.name} - {error.error}</FormLabel>
                    </ListItem>))
              }
            </List>
            {/*Uploaded Files*/}
            <List>
              {
                files.files.map((file, i) => (
                    <ListItem secondaryAction={
                      <IconButton edge="end" aria-label="delete"
                                  onKeyPress={keyboardClick(deleteFile.bind(i))}
                                  onClick={() => deleteFile(i)}>
                        <DeleteIcon/>
                      </IconButton>
                    }>
                      {file.name}
                    </ListItem>
                ))
              }
            </List>
            <Button onKeyPress={keyboardClick(uploadFiles)} onClick={uploadFiles}
                variant="contained"
                color="primary">
              Submit
            </Button>
          </Stack>
        </CardContent>
      </Card>
  );
}

export default UploadImageTab