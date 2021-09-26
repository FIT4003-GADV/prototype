import { Grid, LinearProgress } from '@material-ui/core';
import React, { useEffect, useState } from 'react';
import FileHeader from './FileHeader';

const UploadWithProgress = ({file,onDelete,onUpload}) => {
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    const timer = setInterval(() => {
      setProgress((newProgress) => newProgress >=100 ? 100 : newProgress + 10)
    }, 10)

    return () => {
      onUpload(file)
      clearInterval(timer)
    }
  }, []);

  return (
    <Grid item>
      <FileHeader file={file} onDelete={onDelete} />
      <LinearProgress variant="determinate" value={progress} />
    </Grid>
  );
}

export default UploadWithProgress
