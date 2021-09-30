import { Button, Grid } from '@material-ui/core';
import React from 'react';

const FileHeader = ({ file, onDelete }) => {
  console.log(file)
  return (
    <Grid container justify="space-between" alignItems="center">
      <Grid item>{file.imageInfo.name}</Grid>
      <Grid item>
        <Button size="small" onClick={() => onDelete(file.id)}>
          Delete
        </Button>
      </Grid>
    </Grid>
  );
}

export default FileHeader