import { Button, Grid } from '@material-ui/core';
import React from 'react';

const FileHeader = ({ file, onDelete }) => {
  return (
    <Grid container justify="space-between" alignItems="center">
      <Grid item>{file.name}</Grid>
      <Grid item>
        <Button size="small" onClick={() => onDelete(file)}>
          Delete
        </Button>
      </Grid>
    </Grid>
  );
}

export default FileHeader