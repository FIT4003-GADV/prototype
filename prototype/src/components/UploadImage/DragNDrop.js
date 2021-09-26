import { Grid, makeStyles } from '@material-ui/core';
import { useField } from 'formik';
import React, { useCallback, useEffect, useState } from 'react';
import { useDropzone } from 'react-dropzone';
import UploadWithProgress from './UploadWithProgress';
import UploadError from './UploadError'


let currentId = 0;
const getNewId = () => {
  return ++currentId;
}

const useStyles = makeStyles((theme) => ({
    dropzone: {
      border: `2px dashed ${theme.palette.primary.main}`,
      borderRadius: theme.shape.borderRadius,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      background: theme.palette.background.default,
      height: theme.spacing(10),
      outline: 'none',
    },
  }));

const DragNDrop = ({ name='files' }) => {
    const [_, __, helpers] = useField(name);
    const classes = useStyles();
    const [isHovering, setIsHovering] = useState(false);
    const [files, setFiles] = useState([]);

    console.log(files)

    const onDrop = useCallback((accFiles, rejFiles) => {
      const mappedAcc = accFiles.map((file) => ({ file, errors: [], id: getNewId() }));
      const mappedRej = rejFiles.map((r) => ({ ...r, id: getNewId() }));
      setFiles((curr) => [...curr, ...mappedAcc, ...mappedRej]);
    }, []);
  
    useEffect(() => {
      helpers.setValue(files);
    }, [files]);
  
    const onUpload = (file, url) => {
      setFiles((curr) =>
        curr.map((fw) => {
          if (fw.file === file) {
            return { ...fw, url };
          }
          return fw;
        })
      );
    }
  
    const onDelete = (file) => {
      setFiles((curr) => curr.filter((fw) => fw.file !== file));
    }
  
    const { getRootProps, getInputProps } = useDropzone({
      onDrop,
      accept: ['.svg'],
      maxSize: 300 * 1024, // 300KB
    });
  
    return (
      <>
        <Grid item >
          <div
            onMouseOver={() => setIsHovering(true)}  
            onMouseLeave={() => setIsHovering(false)} 
            style={{backgroundColor: isHovering && '#E8E8E8', cursor: isHovering && 'pointer'}}
            {...getRootProps({ className: classes.dropzone })}
          >
            <input {...getInputProps()} />
            <p>Drag 'n' drop SVG image here, or click to select image</p>
          </div>
        </Grid>
  
        {files.map((fileWrapper) => (
          <Grid item key={fileWrapper.id}>
            {
              fileWrapper.errors.length ? 
              <UploadError
                file={fileWrapper.file}
                errors={fileWrapper.errors}
                onDelete={onDelete}
              /> : 
              <UploadWithProgress
                onDelete={onDelete}
                onUpload={onUpload}
                file={fileWrapper.file}
              />
            }
          </Grid>
        ))}
      </>
    );
  }

  export default DragNDrop
  