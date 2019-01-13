import React from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';
import { withStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Drawer from '@material-ui/core/Drawer';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import IconButton from '@material-ui/core/IconButton';
import Badge from '@material-ui/core/Badge';
import MenuIcon from '@material-ui/icons/Menu';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import NotificationsIcon from '@material-ui/icons/Notifications';
import { mainListItems, secondaryListItems } from './listItems';
import ListItemText from '@material-ui/core/ListItemText';
import InboxIcon from '@material-ui/icons/MoveToInbox';
import MailIcon from '@material-ui/icons/Mail';
import SimpleLineChart from './SimpleLineChart';
import SimpleTable from './SimpleTable';
import styles from './DesktopStyle';
import Wrapper from './Layout/Wrapper';
import Canvas from './Canvas';
import { Paper } from '@material-ui/core';
import A3 from '../assets/images/A3.png'
// import './Desktop.scss';

class Desktop extends React.Component {
  render() {
    const { classes } = this.props;
    const styles = {
      width: 100,
      heigh: 100
    };
    return (
      <Wrapper>
        <Wrapper.AppBar title='A Castro' />
        <Drawer
          className={classes.drawer}
          variant="permanent"
          classes={{
            paper: classes.drawerPaper,
          }}
        >
          <div className={classes.toolbar} />
          <List>
            {['All mail', 'Trash', 'Spam'].map((text, index) => (
              <ListItem button key={text}>
                <Paper>
                  <Typography variant="h6" component="h4">
                    A3
                     </Typography>

                  <img style={styles} src={A3} alt="A3" />

                </Paper>
                {/* <ListItemIcon>{index % 2 === 0 ? <InboxIcon /> : <MailIcon />}</ListItemIcon>
              <ListItemText primary={text} /> */}
              </ListItem>
            ))}
          </List>
        </Drawer>
        <Wrapper.Main >
          <div className={classes.appBarSpacer} />
          <Canvas fragments={[{ id: 1, x:300, y:150 },{ id: 2, x:600, y:220 }]} />
        </Wrapper.Main>
      </Wrapper>
    );
  }
}

Desktop.propTypes = {
  classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(Desktop);