import {
  AppBar,
  Box,
  Container,
  CssBaseline,
  Toolbar,
  Typography,
  Tabs,
  Tab,
} from '@mui/material';
import React, { useState } from 'react';
import UploadImageTab from './components/UploadImage/UploadImageTab';
// import InsertCodeTab from './components/InsertCode/InsertCodeTab';
import IntroSection from './components/IntroSection';
import TabPanel from './components/TabPanel.js';

const App = () =>{
  const [tab, setTab] = useState(0);
  return (
    <>
      <AppBar position="fixed">
        <Toolbar variant="dense">
          <Typography variant="h6">
            Alt Text Generation from SVG
          </Typography>
        </Toolbar>
      </AppBar>
      <CssBaseline />
      <Container maxWidth="lg">
        <IntroSection />
      </Container>
      <Container>
        <Box marginTop={5} sx={{ width: '100%' }}>
          <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
            <Tabs value={tab} onChange={(e, newValue) => setTab(newValue)}>
              <Tab label="Upload SVG image"  />
              <Tab label="Insert XML code" />
            </Tabs>
          </Box>
          <TabPanel value={tab} index={0}>
            <UploadImageTab />
          </TabPanel>
          <TabPanel value={tab} index={1}>
            {/*<InsertCodeTab />*/}
          </TabPanel>
        </Box>
      </Container>
    </>
  );
}

export default App