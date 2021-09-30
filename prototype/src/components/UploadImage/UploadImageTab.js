import {Card, CardContent, makeStyles} from '@mui/material';
import React from 'react';
import Button from "@mui/material/Button";
import Stack from "@mui/material/Stack";

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
    width: '100%',
    "&:focus": {
      backgroundColor: "#E8E8E8"
    }
  },
  hidden: {
    display: "none"
  }
}));

const UploadImageTab = () => {
  const initialData = {files: []}
  const classes = useStyles();

  const fileInput = React.createRef();

  const handleUpload = (event) => {
    if (fileInput.current.files.length === 0 || fileInput.current.files.length > 1) {
      //error wrong number of files
      return;
    }
    const svgFile = fileInput.current.files[0];
    if (svgFile.type !== "image/svg+xml") {
      console.log("wrong file type")
      return;
    }

    console.log(event)
    console.log(fileInput.current)
  };
  return (
    <Card>
      <CardContent>
        <Stack>
          <label className={classes.dropzone} htmlFor="fileInput" tabIndex={0}
                 onKeyDown={document.getElementById("fileInput").click}>
            Drag 'n' drop SVG image here, or click to select image
            <input className={classes.hidden} id="fileInput" type="file" />
          </label>
          <Button
              variant="contained"
              color="primary">
            Submit
          </Button>
        </Stack>
        {/*<Formik*/}
        {/*  initialValues={initialData}*/}
        {/*  validationSchema={validationSchema}*/}
        {/*  onSubmit={submitForm}*/}
        {/*>*/}
        {/*  {({ values, errors, isValid, isSubmitting }) => (*/}
        {/*    <Form>*/}
        {/*      <Grid container spacing={2} direction="column">*/}
        {/*        <DragNDrop name="files" />*/}
        {/*        <Grid item>*/}
        {/*          <Button*/}
        {/*            variant="contained"*/}
        {/*            color="primary"*/}
        {/*            disabled={!isValid || isSubmitting}*/}
        {/*            type="submit"*/}
        {/*          >*/}
        {/*            Submit*/}
        {/*          </Button>*/}
        {/*        </Grid>*/}
        {/*      </Grid>*/}
        {/*      <pre>{values && JSON.stringify({ values, errors }, null, 4)}</pre>*/}
        {/*    </Form>*/}
        {/*  )}*/}
        {/*</Formik>*/}
      </CardContent>
    </Card>
  );
}

export default UploadImageTab