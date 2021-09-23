import { Box, Typography } from '@material-ui/core';

const TabPanel = ({ children, value, index }) => {
    return (
      <div hidden={value !== index}>
        {value === index && (
          <Box sx={{ p: 3 }}>
            <Typography>{children}</Typography>
          </Box>
        )}
      </div>
    );
  }

  export default TabPanel