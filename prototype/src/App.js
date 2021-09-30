import {AppBar, Container, CssBaseline, Toolbar, Typography,} from '@mui/material';
import React from 'react';
// import InsertCodeTab from './components/InsertCode/InsertCodeTab';
import IntroSection from './components/IntroSection';
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import UploadPage from "./components/UploadPage.js";
import ProcessPage from "./components/ProcessPage.js";

const App = () => {
  return (
      <Router>
        <AppBar position="fixed">
          <Toolbar variant="dense">
            <Typography variant="h6">
              Alt Text Generation from SVG
            </Typography>
          </Toolbar>
        </AppBar>
        <CssBaseline/>
        <Container maxWidth="lg">
          <IntroSection/>
        </Container>
        <Switch>
          <Route path="/process">
            <ProcessPage/>
          </Route>
          <Route path="/">
            <UploadPage/>
          </Route>
        </Switch>
      </Router>
  );
}

export default App