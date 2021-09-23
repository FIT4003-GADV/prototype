import {
  AppBar,
  Box,
  Container,
  createStyles,
  CssBaseline,
  makeStyles,
  Toolbar,
  Typography
} from '@material-ui/core';
import React from 'react';
import  Home  from './components/Home';

const useStyles = makeStyles(() =>
  createStyles({
    title: {
      flexGrow: 1,
    },
  })
);

const App = ({ Component, pageProps }) =>{
  const classes = useStyles();
  React.useEffect(() => {
    // Remove the server-side injected CSS.
    const jssStyles = document.querySelector('#jss-server-side');
    if (jssStyles) {
      jssStyles.parentElement.removeChild(jssStyles);
    }
  }, []);

  return (
    <React.Fragment>
    <AppBar position="fixed">
      <Toolbar variant="dense">
        <Typography variant="h6" className={classes.title}>
          ALt Text Generator from SVG
        </Typography>
      </Toolbar>
    </AppBar>
    <CssBaseline />
    <Container>
      <Box marginTop={20}>
        <Home />
      </Box>
    </Container>
</React.Fragment>
  );
}

export default App