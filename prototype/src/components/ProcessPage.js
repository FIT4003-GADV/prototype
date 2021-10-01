import {Box, Card, CardContent, Container,} from '@mui/material';
import React, {useState} from 'react';
import {useLocation} from 'react-router-dom';
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import LinearProgress from '@mui/material/LinearProgress';
import axios from "axios";
import Stack from "@mui/material/Stack";
import IconButton from "@mui/material/IconButton";
import DeleteIcon from "@mui/icons-material/Delete.js";
import Alert from "@mui/material/Alert";

const ProcessPage = () => {
  const [isSent, setSent] = useState(false)

  /* Get the files that we are to upload */
  const location = useLocation()
  let files = []
  if (location.state && 'files' in location.state) {
    files = location.state.files
  }

  const CancelToken = axios.CancelToken
  const [progress, setProgress] = useState(files.map(() => 0))
  const [cancelTokens, setTokens] = useState(files.map(() => CancelToken.source()))

  /* If there were no files */
  if (files.length === 0) {
    return (
        <Container>
          <Card>
            <CardContent>
              <Box marginTop={5} sx={{width: '100%'}}>
                <Alert severity={"warning"}>No Files Selected</Alert>
              </Box>
            </CardContent>
          </Card>
        </Container>)
  }

  /* If we haven't started the post requests, we do that now */
  if (!isSent) {
    console.log("sending")
    files.forEach((file, i) => {
      axios.post("https://httpbin.org/post", file, {
        cancelToken: cancelTokens[i].token,
        onUploadProgress: (p) => {
          progress[i] = Math.round((p.loaded / p.total) * 100)
          setProgress([...progress])
        }
      }).then(result => {
        console.log(`${i} done`)
        console.log(result)
        progress[i] = 100

        /* Simulate Processing */
        setTimeout(() => {
          progress[i] = 101;
          setProgress([...progress])
        }, 2000)

        setProgress([...progress])
      }).catch(error => {
        if (axios.isCancel(error)) {
          console.log("Cancelled request " + i)
        } else {
          console.log('Request Error')
        }
        progress[i] = -1;
        setProgress([...progress])
      })
    });
    setSent(true)
  }

  /* Cancel a file upload */
  const cancelFile = i => cancelTokens[i].cancel("Cancelled by user")

  /* If a space or enter, call function */
  const keyboardClick = func => e => e.keyCode === 13 || e.keyCode === 32 ? func : false

  /* Display the loading bars and the files */
  return (
      <Container>
        <Card>
          <CardContent>
            <List>
              {files.map((file, i) => {
                switch (progress[i]) {
                  case -1: // Failed
                    return (<Alert key={i} severity="error">{i} - {file.name} - Cancelled</Alert>)
                  case 101: // Finished
                    return (<Alert key={i} severity="success">{i} - {file.name} - Finished</Alert>)
                  default: // In progress
                    return (
                        <ListItem key={i} sx={{width: '100%'}} secondaryAction={
                          <IconButton edge="end" aria-label={`Cancel file ${file.name}`}
                                      onKeyPress={keyboardClick(cancelFile.bind(i))}
                                      onClick={() => cancelFile(i)}>
                            <DeleteIcon/>
                          </IconButton>
                        }>
                          <Stack sx={{width: '100%'}}>
                            {i} - {file.name} - {progress[i]}%
                            <LinearProgress color={progress[i] === -1 ? "secondary" : "primary"}
                                            variant={progress[i] === 100 ? "indeterminate" : "determinate"}
                                            value={progress[i]} aria-label={`${file.name} progress`}/>
                          </Stack>
                        </ListItem>)
                }
              })}
            </List>
          </CardContent>
        </Card>
      </Container>
  );
}

export default ProcessPage