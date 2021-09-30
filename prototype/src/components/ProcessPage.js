import {Box, Container,} from '@mui/material';
import React, {useState} from 'react';
import {useLocation} from 'react-router-dom';
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import LinearProgress from '@mui/material/LinearProgress';
import axios from "axios";
import Stack from "@mui/material/Stack";

const ProcessPage = () => {
  const location = useLocation()
  const [isSent, setSent] = useState(false)

  let files = []
  if (location.state && 'files' in location.state) {
    files = location.state.files
  }
  const [progress, setProgress] = useState(files.map(() => 0))

  if (files.length === 0) {
    return (<Container>
      <Box marginTop={5} sx={{width: '100%'}}>
        ERROR NO FILES
      </Box>
    </Container>)
  }

  if (!isSent) {
    console.log("sending")
    files.forEach((file, i) => {
      axios.request({
        method: "post",
        url: "https://httpbin.org/post",
        data: file,
        onUploadProgress: (p) => {
          progress[i] = Math.round((p.loaded / p.total) * 100)
          setProgress([...progress])
        }
      }).then(data => {
        console.log(`${i} done`)
        progress[i] = 100
        setProgress([...progress])
      })
    });
    setSent(true)
  }

  return (
      <Container>
        <Box marginTop={5} sx={{width: '100%'}}>
          <List>
            {files.map((file, i) => (
                <ListItem key={i} sx={{ width: '100%' }}>
                  <Stack sx={{ width: '100%' }}>
                    {i} - {file.name} - {progress[i]}%
                    <LinearProgress variant="determinate" value={progress[i]}/>
                  </Stack>
                </ListItem>
            ))}
          </List>
        </Box>
      </Container>
  );
}

export default ProcessPage