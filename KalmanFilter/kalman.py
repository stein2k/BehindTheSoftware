import numpy as np

def main():

    # Example from the Wikipedia article on Kalman filtering
    # Consider a truck on frictionless, straight rails.
    # Initially, the truck is stationary at position 0, but
    # it is buffeted this way and that by random uncontrolled 
    # forces. We measure the position of the truck every delta_t 
    # seconds, but these measurements are imprecise; we want 
    # to maintain a model of where the truck is and what its 
    # velocity is. We show here how we derive the model from 
    # which we create our Kalman filter.
    F = np.array(((1,1),(0,1)),dtype=np.float64)
    H = np.array(((1,0),),dtype=np.float64)

    # Initial state
    x = np.array(((0,),(0,)),dtype=np.float64)

    sigma_a = 0.1
    sigma_z = 0.1

    x_est = np.array(((0,),(0,)),dtype=np.float64)
    P_est = np.array(((0,0),(0,0)),dtype=np.float64)

    for n in range(100):

        # Update position and velocity of truck
        x = np.dot(F,x) + np.dot(np.array(((np.sqrt(sigma_a/4.0),0),
            (0,np.sqrt(sigma_a))),dtype=np.float64),np.random.randn(2,1))

        # Observe truck position
        z = np.dot(H,x) + np.sqrt(sigma_z)*np.random.randn()

        # Time Update (Prediction)
        x_est = np.dot(F,x_est)
        P_est = (np.dot(F,np.dot(P_est,F.T)) + np.eye(2))

        # Update
        y = z - np.dot(H,x_est)
        S = np.dot(H,np.dot(P_est,H.T)) + np.eye(1)

        print "P_est =", P_est
        print "H.T =", H.T, ", P_est*H.T =", np.dot(P_est,H.T)
        print "S =", S

        K = np.dot(np.dot(P_est,H.T),np.linalg.inv(S))
        x_est = x_est + np.dot(K,y)
        P_est = np.dot((np.eye(2)-np.dot(K,H)),P_est)
        
        print 'x =', x
        print 'y =', y
        print 'x_est =', x_est

if __name__ == '__main__':
    main()
