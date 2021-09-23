import {
  AppBar,
  Box,
  Container,
  CssBaseline,
  Toolbar,
  Typography,
  Tabs,
  Tab,
} from '@material-ui/core';
import React, { useState } from 'react';
import UploadImageTab from './components/UploadImage/UploadImageTab';
import InsertCodeTab from './components/InsertCode/InsertCodeTab';
import IntroSection from './components/IntroSection';

const TabPanel = ({ children, value, index, ...other }) => {
  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box sx={{ p: 3 }}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  );
}

const a11yProps = (index) => {
  return {
    id: `simple-tab-${index}`,
    'aria-controls': `simple-tabpanel-${index}`,
  };
}

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
              <Tab label="Upload SVG image" {...a11yProps(0)} />
              <Tab label="Insert XML code" {...a11yProps(1)} />
            </Tabs>
          </Box>
          <TabPanel value={tab} index={0}>
            <UploadImageTab />
          </TabPanel>
          <TabPanel value={tab} index={1}>
            <InsertCodeTab />
          </TabPanel>
        </Box>
      </Container>
    </>
  );
}

export default App