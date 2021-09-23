import {
  AppBar,
  Box,
  Container,
  createStyles,
  CssBaseline,
  makeStyles,
  Toolbar,
  Typography,
  Tabs,
  Tab,
} from '@material-ui/core';
import React, { useState } from 'react';
import Home from './components/UploadImage/UploadImageTab';

const useStyles = makeStyles(() =>
  createStyles({
    title: {
      flexGrow: 1,
    },
  })
);

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
  const classes = useStyles();

  return (
    <React.Fragment>
    <AppBar position="fixed">
      <Toolbar variant="dense">
        <Typography variant="h6" className={classes.title}>
          Alt Text Generation from SVG
        </Typography>
      </Toolbar>
    </AppBar>
    <CssBaseline />
    <Container>
      <Box marginTop={10} sx={{ width: '100%' }}>
        <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
          <Tabs value={tab} onChange={(e, newValue) => setTab(newValue)} aria-label="basic tabs example">
            <Tab label="Upload SVG image" {...a11yProps(0)} />
            <Tab label="Insert XML code" {...a11yProps(1)} />
          </Tabs>
        </Box>
        <TabPanel value={tab} index={0}>
          <Home />
        </TabPanel>
        <TabPanel value={tab} index={1}>
          Item Two
        </TabPanel>
      </Box>
    </Container>
</React.Fragment>
  );
}

export default App